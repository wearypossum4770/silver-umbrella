import { mount } from "@vue/test-utils";
import { render } from "@testing-library/vue";
import LoginForm from "../../src/components/LoginForm";

beforeAll(() => jest.spyOn(window, "fetch"));
