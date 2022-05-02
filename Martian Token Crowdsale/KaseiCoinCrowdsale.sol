pragma solidity ^0.5.0;

//  Importing KaseiCoin contract and the following contracts from the OpenZeppelin library:
//    * `Crowdsale`
//    * `MintedCrowdsale`
//    * `CappedCrowdsale`
//    * `TimedCrowdsale`
//    * `RefundablePostDeliveryCrowdsale`   
import "KaseiCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";

// Defing the KaseiCoin contract that inherits Crowdsale, MintedCrowdsale, CappCappedCrowdsale, TimedCrowdsale and RefundablePostDeliveryCrowdsale
contract KaseiCoinCrowdsale is Crowdsale, MintedCrowdsale, CappedCrowdsale, TimedCrowdsale, RefundablePostDeliveryCrowdsale { 
    // Building the constructor for KaseiCoinCrowdsale 
    constructor(uint rate, address payable wallet, KaseiCoin token, uint goal, uint open, uint close) 
    Crowdsale(rate, wallet, token)
    CappedCrowdsale(goal)
    TimedCrowdsale(open,close)
    RefundableCrowdsale(goal)
    public {}
}

// Defining the Deployer contract for KaseiCoin and KaseiCoinCrowdsale contracts
contract KaseiCoinCrowdsaleDeployer {
    // Defining a variable to store the KaseiCoin contract's address
    address public kasei_token_address;
    // Defining a variable to store the KaseiCoinCrowdsale contract's address
    address public kasei_crowdsale_address;

    // Defing the Deployer constructor 
    constructor(
       string memory name,
       string memory symbol,
       address payable wallet,
       uint goal
    ) public {
        // Creating a new instance of the 'KaseiCoin' contract and assigning the token contract's address to the `kasei_token_address` variable. 
        KaseiCoin token = new KaseiCoin(name, symbol, 0);
        kasei_token_address = address(token);

        // Creating a new instance of the 'KaseiCoinCrowdsale' contract and assigning the token contract's address to the `kasei_crowdsale_address` variable.
        KaseiCoinCrowdsale kasei_crowdsale = new KaseiCoinCrowdsale(1, wallet, token, goal, now, now + 20 minutes);
        kasei_crowdsale_address = address(kasei_crowdsale);

        // Setting the `KaseiCoinCrowdsale` contract as a minter
        token.addMinter(kasei_crowdsale_address);
        
        // Have the `KaseiCoinCrowdsaleDeployer` renounce its minter role.
        token.renounceMinter();
    }
}