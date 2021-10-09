<template>
  <div class="stack-small" v-if="!isEditing">
    <div class="custom-checkbox">
      <input
        type="checkbox"
        class="checkbox"
        :id="id"
        :checked="isDone"
        @change="$emit('checkbox-changed')"
      />
      <label :for="id" class="checkbox-label"
        ><span itemprop="itemListElement">{{ label }}</span></label
      >
    </div>
    <div class="btn-group">
      <button
        type="button"
        ref="editButton"
        class="btn"
        @click="toggleToItemEditForm"
      >
        Edit <span class="visually-hidden">{{ label }}</span>
      </button>
      <button type="button" class="btn btn__danger" @click="deleteToDo">
        Delete <span class="visually-hidden">{{ label }}</span>
      </button>
    </div>
  </div>
  <to-do-item-edit-form
    v-else
    :id="id"
    :label="label"
    @item-edited="itemEdited"
    @edit-cancelled="editCancelled"
  ></to-do-item-edit-form>
</template>
<script>
import ToDoItemEditForm from "./ToDoItemEditForm";
export default {
  name: "TodoItem",
  components: { ToDoItemEditForm },
  data() {
    return {
      isEditing: false,
    };
  },
  props: {
    label: { required: true, type: String },
    done: { default: false, type: Boolean },
    id: { required: true, type: String },
  },
  computed: {
    isDone() {
      return this.done;
    },
  },
  methods: {
    itemEdited(newLabel) {
      this.$emit("item-edited", newLabel);
      this.isEditing = false;
      this.focusOnEditButton();
    },
    editCancelled() {
      this.isEditing = false;
      this.focusOnEditButton();
    },
    deleteToDo() {
      this.$emit("item-deleted");
    },
    focusOnEditButton() {
      this.$nextTick(() => this.$refs.editButton.focus());
    },
    toggleToItemEditForm() {
      this.isEditing = true;
    },
  },
};
</script>
<style scoped></style>
