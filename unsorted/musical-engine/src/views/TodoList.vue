<template>
  <div class="custom-checkbox">
    <h1>To-Do List</h1>
    <create-todo @todo-added="addToDo"></create-todo>
    <h2 id="list-summary" ref="listSummary" tabindex="-1">{{ listSummary }}</h2>
    <ul
      type="none"
      id="todo-list-items"
      aria-labelledby="list-summary"
      class="stack-large"
    >
      <li v-for="item in todos" :key="item.id">
        <to-do-item
          :label="item.label"
          :done="item.done"
          :id="item.id"
          @checkbox-changed="updateDoneStatus(item.id)"
          @item-deleted="deleteByID(item.id)"
          @item-edited="editByID(item.id, $event)"
        ></to-do-item>
      </li>
    </ul>
  </div>
</template>
<script>
// import uniqueId from "lodash.uniqueid";
import CreateTodo from "../components/todo/CreateTodo";
import ToDoItem from "../components/todo/ToDoItem.vue";
export default {
  name: "TodoList",
  components: {
    ToDoItem,
    CreateTodo,
  },
  methods: {
    findByID(_id) {
      return this.todos.find(item => item.id === _id);
    },
    deleteByID(_id) {
      const id = this.findByID(_id);
      this.todos.splice(id, 1);
      this.$refs.listSummary.focus();
    },
    editByID(_id, newLabel) {
      const todo = this.findByID(_id);
      todo.label = newLabel;
    },
    getNextID() {
      let _id = 1;
      let ids = this.todos.map(todo => parseInt(todo.id?.match(/\d+/).shift()));
      if (ids.length > 0) {
        let last = ids.pop();
        _id = last += 1;
      }
      return _id;
    },
    updateDoneStatus(_id) {
      const toDoToUpdate = this.findByID(_id);
      toDoToUpdate.done = !toDoToUpdate.done;
    },
    addToDo(toDoLabel) {
      this.todos.push({
        id: `todo-${this.getNextID()}`,
        label: toDoLabel,
        done: false,
      });
    },
  },
  computed: {
    doneTodos() {
      return this.todos?.filter(item => item.done);
    },
    todoList() {
      if (this.hideCompletedTodos) {
        return this.todos?.filter(item => !item.done);
      } else {
        return this.todos;
      }
    },
    listSummary() {
      const completed = this.doneTodos.length;
      return `${completed} out of ${this.todos.length} items completed`;
    },
  },
  data() {
    return {
      hideCompletedTodos: false,
      todos: [],
    };
  },
};
</script>
<style scoped></style>
