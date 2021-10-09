<template>
  <div>
    <div id="dropzone" v-on:drop="handleDrop" v-on:dragover="allowDrop">
      Drop Zone
    </div>
    <div>
      <div>
        <div><input v-on:change="attachFile" type="file" /></div>
        <button v-on:click="sendToBackend">Submit</button>
      </div>
    </div>
    <div className="dropzone">
      <img
        id="image"
        v-on:dragstart="handleDrag"
        draggable="true"
        src="@/assets/img_logo.gif"
        width="336"
        height="69"
      />
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      formData: new FormData(),
      uploads: [],
      image: null,
      dragged: null,
    };
  },
  methods: {
    attachFile({ target: { files } }) {
      const file = files[0];
      this.uploads.push(file.name);
      this.formData.append(file.name, file);
    },
    handleSubmit(e) {
      e.preventDefault();
    },
    handleDragStart(e) {
      console.log(e);
    },
    handleDragEnd(e) {
      console.log(e);
    },
    async sendToBackend() {},
    handleFile({ target }) {
      console.log(target.files);
    },
    handleDrop(e) {
      let { dataTransfer } = e;
      e.preventDefault();
      const isImage = dataTransfer.getData("URL");
      if (isImage !== "") {
        this.uploads.push(isImage);
      }
      if (dataTransfer.items && isImage === "") {
        for (let i = 0; i < dataTransfer.items.length; i++) {
          if (dataTransfer.items[i].kind === "file") {
            this.uploads.push(dataTransfer.items[i].getAsFile());
          }
        }
      }
    },
    allowDrop(e) {
      e.preventDefault();
    },
    handleClick(e) {
      console.log(e);
    },
    dropHandler(e) {
      e.preventDefault();
    },
    handleDrag({ dataTransfer }) {
      this.dragged = dataTransfer.getData("URL");
    },
  },
};
</script>
<style>
#draggable {
  width: 200px;
  height: 20px;
  text-align: center;
  background: white;
}
.dropzone {
  width: 200px;
  height: 20px;
  background: blueviolet;
  margin-bottom: 10px;
  padding: 10px;
}
</style>
