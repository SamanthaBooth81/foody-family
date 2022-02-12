function deleteIngredient(target) {
    divId = target.getAttribute('data-ingredient-id')
    document.getElementById(divId).remove();
}

document.addEventListener("DOMContentLoaded", function () {
    let ingredientsCounter = 0;


    function add_ingredients(event) {
        ingredientId = 'ingredient_' + ingredientsCounter;
        new_ingredient = '<div class="add-ingredient" id="' + ingredientId + '"> <input type="text" name="ingredients"> <button type="button" onClick="deleteIngredient(this)" class="delete_ingredient" data-ingredient-id="' + ingredientId + '">Delete</button></div>';
        ingredientsCounter = ingredientsCounter + 1;
        let newingredient = document.createElement('div');
        newingredient.innerHTML = new_ingredient;
        document.getElementById('ingredients_list').appendChild(newingredient);
    }


    document.getElementById('add_ingredients').addEventListener('click', add_ingredients);

});

function deleteInstruction(target) {
    divId = target.getAttribute('data-instruction-id')
    document.getElementById(divId).remove();
}


document.addEventListener("DOMContentLoaded", function () {
    let instructionsCounter = 0;


    function add_instruction(event) {
        instructionId = 'instruction_' + instructionsCounter;
        new_instruction = '<div class="add-instruction" id="' + instructionId + '"> <input type="text" name="instructions"> <button type="button" onClick="deleteInstruction(this)" class="delete_instruction" data-instruction-id="' + instructionId + '">Delete</button></div>';
        instructionsCounter = instructionsCounter + 1;
        let newdiv = document.createElement('div');
        newdiv.innerHTML = new_instruction;
        document.getElementById('step_list').appendChild(newdiv);
    }


    document.getElementById('add_step').addEventListener('click', add_instruction);


});