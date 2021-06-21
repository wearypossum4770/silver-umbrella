import React from 'react'
    
/**
* Renders a <Button /> component
* @param  props
* @param  props.textColor - the color of the text in the button
* @param  props.bgColor - the background color of the button
* @param  props.overrideStyles - used to set the CSS of the button
*/
export const Button = ({ textColor, bgColor, overrideStyles =  ) => (
  <button
    style={{
      color: textColor,
      backgroundColor: bgColor,
      ...overrideStyles
    }}
  >
    {children}
  </button>
)

/**
 * @typedef People
 * @prop {string} firstName
 * @prop {string} [lastName] 
 */

 /**
  * @typedef {{firstName: string, lastName: string}} PeopleTwo
  */

  /**
   * @param {People} people 
   */
   function getPeopleName(people){
    return people.firstName;
  }