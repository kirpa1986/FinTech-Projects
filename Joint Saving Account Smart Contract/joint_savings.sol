pragma solidity ^0.5.0;

// Defining a new contract named `JointSavings`
contract JointSavings {

    
    // Defining the contract variables
    address payable accountOne;
    address payable accountTwo;
    address public lastToWithdraw;
    uint public lastWithdrawAmount;
    uint public contractBalance; 
    
    // Function to withdraw Ether from the joint account
    function withdraw(uint amount, address payable recipient) public {

        // Checking if the recepient is on of the joint account owners
        require(recipient == accountOne || recipient == accountTwo, "This withdrawal can't be processed! Reason: You don't own this account!");

        // Checking the balance is greater than the requested for withdrawal
        require(contractBalance > amount, "This withdrawal can't be processed! Reason: Insufficient funds!" );

        // Updating the last recipient if it's not the current
        if (recipient != lastToWithdraw) {
            lastToWithdraw = recipient;
        }

        // Transfering the amount to the recipient after all required checks are passed
        recipient.transfer(amount);

        // Updating lastWithdrawAmount with the requested for withdrawal amount
        lastWithdrawAmount = amount;

        // Call the `contractBalance` variable and set it equal to the balance of the contract by using `address(this).balance` to reflect the new balance of the contract.
        contractBalance = address(this).balance;

    }

    // Defining a deposit function that will deposit funds to the joint account
    function deposit() public payable {
        // Setting the contract balance equal to the balance of the contract
        contractBalance = address(this).balance;
    }

    // Defining both accounts for the joint account
    function setAccounts(address payable account1, address payable account2) public{
        accountOne = account1;
        accountTwo = account2;
    }

    
    // Difining the default fallback function so the your contract can store Ether sent from outside the deposit function.
    function() external payable {
        contractBalance = address(this).balance;
    }
}