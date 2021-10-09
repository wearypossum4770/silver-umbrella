let examples = [
  {categoryName:"Machinery and Equipment", category:"machinery_and_equipment",	  description:"Books and Multimedia Materials", usefulLife:5},
  {categoryName:"Machinery and Equipment", category:"machinery_and_equipment",	  description:"Computer Equipment", usefulLife:5},
  {categoryName:"Licensed Vehicles", category:"licensed_vehicles", description:"General Automobile", usefulLife:	8},
  {categoryName:"Machinery and Equipment", category:"machinery_and_equipment",	  description:"Science and Engineering Equipment", usefulLife:10},
  {categoryName:"Machinery and Equipment", category:"machinery_and_equipment",	  description:"Audiovisual Equipment", usefulLife:10},
  {categoryName:"Machinery and Equipment", category:"machinery_and_equipment",	  description:"Athletic Equipment", usefulLife:10},
  {categoryName:"Machinery and Equipment", category:"machinery_and_equipment",	  description:"Grounds and Maintenance Equipment", usefulLife:15},
 {categoryName:"Land Improvements",category:"land_improvements",	 description: "Fencing"	,usefulLife:20},
 {categoryName:"Machinery and Equipment", category:"machinery_and_equipment",	  description:"Playground Structures"	,usefulLife:20},
]
const straingLineDepreciation = (originalCost=0,salvageValue=0, usefulLife=0) => (originalCost-salvageValue)/usefulLife
let obj = straingLineDepreciation (21_500,0,20)

console.log(obj)
