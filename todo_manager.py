import flet as ft
import json

def main(page: ft.Page):
    page.title = "To-Do Manager"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # 할 일 리스트를 저장할 리스트
    todo_list = []

    # 필터링 옵션: 'All', 'Completed', 'Pending'
    filter_options = ['All', 'Completed', 'Pending']
    current_filter = filter_options[0]

    # 할 일 리스트를 업데이트하는 함수
    def update_todo_list():
        # 선택된 필터 옵션에 따라 리스트를 필터링
        filtered_list = [
            todo for todo in todo_list
            if (current_filter == 'All' or
                (current_filter == 'Completed' and todo['completed']) or
                (current_filter == 'Pending' and not todo['completed']))
        ]
        # 완료된 할 일은 하단으로 이동
        filtered_list.sort(key=lambda x: x['completed'])
        # 리스트 뷰를 업데이트
        todo_column.controls.clear()
        for todo in filtered_list:
            todo_column.controls.append(create_todo_row(todo))
        page.update()

    # 할 일 항목을 생성하는 함수
    def create_todo_row(todo):
        return ft.Row(
            controls=[
                ft.Checkbox(
                    label=todo['title'],
                    value=todo['completed'],
                    on_change=lambda e: toggle_todo_completed(todo),
                ),
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    on_click=lambda e: edit_todo_item(todo),
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    on_click=lambda e: delete_todo_item(todo),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

    # 할 일 완료 여부 토글
    def toggle_todo_completed(todo):
        todo['completed'] = not todo['completed']
        save_todos_to_file()
        update_todo_list()

    # 할 일 추가 기능
    def add_todo_item(e):
        if new_todo.value:
            todo_list.append({
                'title': new_todo.value,
                'completed': False,
            })
            new_todo.value = ""
            save_todos_to_file()
            update_todo_list()

    # 할 일 수정 기능
    def edit_todo_item(todo):
        def save_edit(e):
            todo['title'] = edit_todo_field.value
            page.close(edit_dialog)
            save_todos_to_file()
            update_todo_list()

        edit_todo_field = ft.TextField(value=todo['title'])
        edit_dialog = ft.AlertDialog(
            title=ft.Text("Edit To-Do"),
            content=edit_todo_field,
            actions=[
                ft.ElevatedButton("Save", on_click=save_edit)
            ]
        )
        page.dialog = edit_dialog
        edit_dialog.open = True
        page.update()

    # 할 일 삭제 기능
    def delete_todo_item(todo):
        todo_list.remove(todo)
        save_todos_to_file()
        update_todo_list()

    # 필터 변경 이벤트 처리
    def filter_changed(e):
        nonlocal current_filter
        current_filter = filter_dropdown.value
        update_todo_list()

    # 할 일 리스트를 JSON 파일에 저장하는 함수
    def save_todos_to_file():
        with open("todos.json", "w") as f:
            json.dump(todo_list, f, indent=4)

    # JSON 파일에서 할 일 리스트를 불러오는 함수
    def load_todos_from_file():
        try:
            with open("todos.json", "r") as f:
                global todo_list
                todo_list = json.load(f)
        except FileNotFoundError:
            pass

    # UI 요소 생성
    new_todo = ft.TextField(hint_text="Enter a new task", width=300)
    add_todo_btn = ft.ElevatedButton(text="Add", on_click=add_todo_item)
    filter_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(opt) for opt in filter_options],
        value=current_filter,
        on_change=filter_changed,
    )
    todo_column = ft.Column()

    # 페이지에 UI 요소 추가
    page.add(
        ft.Column(
            controls=[
                ft.Row([new_todo, add_todo_btn]),
                filter_dropdown,
                todo_column,
            ]
        )
    )

    # 초기 데이터 로드 및 UI 업데이트
    load_todos_from_file()
    update_todo_list()

# 앱 실행
ft.app(target=main)
