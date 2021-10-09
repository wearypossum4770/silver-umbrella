import Chat from "../../src/views/Chat.vue";
import { mount } from "@vue/test-utils";

describe("Chat component", () => {
  test("", () => expect(true).toBe(true));
  const wrapper = mount(Chat, {
    propsData: {
      messageList: [{ id: 1 }],
      user: {
        first_name: "ichigo",
        middle_name: "",
        last_name: "kurosaki",
        username: "ichigo.kurosaki",
        password: "password123!@#",
        email: "ichigo.kurosaki@humans.com",
      },
    },
  });
  console.log(wrapper);
});
