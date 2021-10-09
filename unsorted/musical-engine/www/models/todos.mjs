import { Sequelize } from "sequelize";
const { STRING, BOOLEAN, DATE, ENUM } = Sequelize.DataTypes;
const projectSchema = {
  dateStarted: { type: DATE },
  title: { type: STRING },
  description: { type: STRING },
  createdBy,
  dateEnded: { type: DATE },
  status: ENUM(
    "completed",
    "draft",
    "deleted",
    "archived",
    "bloacked",
    "inprogress",
  ),
};
const todoSchema = {
  content: { type: STRING },
  title: { type: STRING },
  isCompleted: { type: BOOLEAN },
  dateDue: { type: DATE },
  dateCompleted: { type: DATE },
  status: ENUM(
    "completed",
    "draft",
    "deleted",
    "archived",
    "bloacked",
    "inprogress",
  ),
  // priority,
  // queue,
  // subprocess,
  // projectId,
};
export default {
  projectSchema,
  todoSchema,
};
