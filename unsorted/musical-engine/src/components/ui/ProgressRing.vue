<template>
  <div>
    <!-- https://css-tricks.com/building-progress-ring-quickly/ -->
    <svg class="progress-ring" width="120" height="120">
      <circle
        class="progress-ring__circle"
        stroke="white"
        stroke-width="4"
        fill="transparent"
        r="52"
        cx="60"
        cy="60"
      />
    </svg>
  </div>
</template>

<script>
export default {
  name: "Progress Ring",
};
</script>

<style scoped>
.progress-ring__circle {
  stroke-dasharray: 10 20;
}
html,
body {
  background-color: #2962ff;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  position: relative;
}
</style>
