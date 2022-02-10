// Below from Code Institutes CodeStar project

// CAUSING AN ERROR IN CONSUL 
// setTimeout(function() {
//     let messages = document.getElementById('msg');
//     let alert = new bootstrap.Alert(messages);
//     alert.close()}, 3000);

function deleteInstruction(target){
    divId = target.getAttribute('data-instruction-id')
    document.getElementById(divId).remove();
}


document.addEventListener("DOMContentLoaded", function() {
    let instructionsCounter = 0;


    function add_instruction(event){
        // console.log('add');
        instructionId = 'instruction_' + instructionsCounter;
        new_instruction = '<div style="margin-top: 5px; margin-left: 15px;" id="' + instructionId + '"> <input type="text" name="instructions[]"> <button type="button" onClick="deleteInstruction(this)" class="delete_instruction" data-instruction-id="'+ instructionId +'">Delete</button></div>';
        instructionsCounter = instructionsCounter + 1;
        let newdiv = document.createElement('div');
        newdiv.innerHTML = new_instruction;
        document.getElementById('step_list').appendChild(newdiv);
    }

   
    document.getElementById('add_step').addEventListener('click', add_instruction);
});
