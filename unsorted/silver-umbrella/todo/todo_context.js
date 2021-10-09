import { createContext } from "react";
export const TodoContext = createContext();
export default function TodoContextProvider({ children }) {
  return (
    <TodoContextProvider.Provider>{children}</TodoContextProvider.Provider>
  );
}
