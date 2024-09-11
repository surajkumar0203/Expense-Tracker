const expense_id = document.getElementById('expense-id')
const expense_name = document.getElementById('expense-name')
const expense_amount = document.getElementById('expense-amount')
const expense_category = document.getElementById('expense-category')


const editFunction=(uuid) =>{
    const row = document.querySelector(`tr[data-id="${uuid}"]`)
    // Get data from the row
    const expenseName =  row.getAttribute("data-name");
    const expenseAmount = row.getAttribute("data-amount");
    const expenseCategory = row.getAttribute("data-category");
    
    // set value input field
    expense_id.value=uuid
    expense_name.value=expenseName
    expense_amount.value=expenseAmount
    expense_category.value=expenseCategory
  
}




