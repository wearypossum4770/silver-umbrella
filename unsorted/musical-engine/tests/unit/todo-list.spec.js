import { mount } from "@vue/test-utils";
import { render } from "@testing-library/vue";
import TodoList from "../../src/views/TodoList.vue";
import ToDoItem from "../../src/components/todo/ToDoItem.vue";
import CreateTodo from "../../src/components/todo/CreateTodo.vue";
import todoList from "../todoList.json";
describe("TodoList component", () => {
  let wrapper = mount(TodoList, {
    data() {
      return { todos: todoList };
    },
  });
  let header2Text = "To-Do List";
  it("has a <h2> tag", async () => {
    const { getByText } = render(TodoList);
    let header2 = getByText(header2Text).textContent;
    expect(header2).toBe(header2Text);
  });
  test("data props are rendered", async () => {
    let todoArray = wrapper.findAll('[itemprop="itemListElement"]');
    expect(todoArray.length).toBe(4);
  });
  test("Checkbox operation", async () => {
    let todoArray = wrapper.findAllComponents(ToDoItem).at(0);
    let input = todoArray.find('input[type="checkbox"]');
    expect(input.element.checked).toBe(false);
    await input.setChecked();
    expect(input.element.checked).toBe(true);
  });
  it("should add new items to todo list", async () => {
    let component = wrapper.findComponent(CreateTodo);
    let textInput = component.find('[name="new-todo"]');
    let todoArrayPre = wrapper.findAll('[itemprop="itemListElement"]');
    await textInput.setValue("Add test to vue project");
    await component.trigger("submit");
    let todoArrayPost = wrapper.findAll('[itemprop="itemListElement"]');
    expect(todoArrayPre.length).toBe(4);
    expect(todoArrayPost.length).toBe(5);
  });
});
