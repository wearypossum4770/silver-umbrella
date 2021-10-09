<template>
  <div>
    <div @keyup.enter.native="handleSubmit" class="card">
      <img
        src="@/assets/groceries/fruits/honey_crisp_apple.jpeg"
        alt="Avatar"
        style="width: 100%"
      />
      <div class="container">
        <input v-model="userInput" @focus="startTimer" @blur="endTimer" />
        <button @click="handleSubmit">Enter</button>
        <p>Architect & Engineer</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PLUCodes",
  methods: {
    handleSubmit() {
      this.isCorrect = this.item.code.toString() === this.userInput;
      this.item.timeSpent = this.item.endTime - this.item.startTime;
    },
    startTimer() {
      this.item.startTime = new Date();
    },
    endTimer() {
      this.item.endTime = new Date();
    },
  },
  data() {
    return {
      isCorrect: false,
      userInput: "",
      item: {
        code: 3283,
        category: "Fruits",
        image: "@/assets/groceries/fruits/honey_crisp_apple.jpeg",
        commodity: "apples",
        variety: "Honeycrisp",
        prices: [{ store: "walmart", price: 4.68, unit: "weight" }],
      },
    };
  },
};
</script>

<style scoped></style>
