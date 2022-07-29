// Given the Node class from `represenation.js`
//

const depthFirstValues = (root) => {
   const stack = [root];
   while ( stack.length > 0 ) {
      const current = stack.pop()
      console.log(current.val);
      if (current.left !== null) {
         stack.push(current.left);
      }
      if (current.right !== null) {
         stack.push(current.right);
      }
   }

}
