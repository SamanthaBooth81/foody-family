// widgets for adding ingredients and deleting ingredient input elements

function deleteIngredient(target) {
    divId = target.getAttribute('data-ingredient-id');
    document.getElementById(divId).remove();
}


document.addEventListener("DOMContentLoaded", function () {
    let ingredientsCounter = 0;

    function add_ingredients(event) {
        // help received from Code Institute tutor Sean with applying querySelector
        const ingredientsCount = document.querySelectorAll("#ingredients_list input").length;
        const ingredientsID = ingredientsCount + 1;
        ingredientId = 'ingredient_' + ingredientsID;
        new_ingredient = '<div class="add-ingredient" id="' + ingredientId + '"> <input type="text" name="ingredients"> <button type="button" onClick="deleteIngredient(this)" class="delete_ingredient" data-ingredient-id="' + ingredientId + '">Delete</button></div>';
        ingredientsCounter = ingredientsCounter + 1;
        let newingredient = document.createElement('div');
        newingredient.innerHTML = new_ingredient;
        document.getElementById('ingredients_list').appendChild(newingredient);
    }

    function add_new_ingredient(event) {
        const ingredientsCount = document.querySelectorAll("#ingredients_list input").length;
        const ingredientsID = ingredientsCount + 1;
        ingredientId = 'ingredient_' + ingredientsID;
        new_ingredient = '<div class="add-ingredient" id="' + ingredientId + '"> <input type="text" name="ingredients"> <button type="button" onClick="deleteIngredient(this)" class="delete_ingredient" data-ingredient-id="' + ingredientId + '">Delete</button></div>';
        ingredientsCounter = ingredientsCounter + 1;
        let newingredient = document.createElement('div');
        newingredient.innerHTML = new_ingredient;
        document.getElementById('ingredients_list').appendChild(newingredient);
    }



    document.getElementById('add_ingredients', ).addEventListener('click', add_ingredients, add_new_ingredient);

});

// widgets for adding instructions and deleting instruction textarea elements

function deleteInstruction(target) {
    divId = target.getAttribute('data-instruction-id');
    document.getElementById(divId).remove();
}


document.addEventListener("DOMContentLoaded", function () {

    let instructionsCounter = 0;


    function add_instruction(event) {
        const instructionCount = document.querySelectorAll("#step_list textarea").length;
        const ingredientID = instructionCount + 1;
        instructionId = 'instruction_' + ingredientID;
        new_instruction = '<div class="add-instruction" id="' + instructionId + '"> <textarea name="instructions" cols="30" rows="3" class="instructions"></textarea> <button type="button" onClick="deleteInstruction(this)" class="delete_instruction" data-instruction-id="' + instructionId + '">Delete</button></div>';
        instructionsCounter = instructionsCounter + 1;
        let newdiv = document.createElement('div');
        newdiv.innerHTML = new_instruction;
        document.getElementById('step_list').appendChild(newdiv);
    }

    function add_new_instruction(event) {
        const instructionCount = document.querySelectorAll("#step_list textarea").length;
        const ingredientID = instructionCount + 1;
        ingredientId = 'ingredient_' + ingredientID;
        new_ingredient = '<div class="add-ingredient" id="' + ingredientId + '"> <textarea name="ingredients" cols="30" rows="3"  class="instructions"></textarea> <button type="button" onClick="deleteIngredient(this)" class="delete_ingredient" data-ingredient-id="' + ingredientId + '">Delete</button></div>';
        ingredientsCounter = ingredientsCounter + 1;
        let newingredient = document.createElement('div');
        newingredient.innerHTML = new_ingredient;
        document.getElementById('ingredients_list').appendChild(newingredient);
    }


    document.getElementById('add_step').addEventListener('click', add_instruction, add_new_instruction);

});