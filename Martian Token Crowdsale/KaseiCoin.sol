pragma solidity ^0.5.0;

//  Importing the following contracts from the OpenZeppelin library:
//    * `ERC20`
//    * `ERC20Detailed`
//    * `ERC20Mintable`
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

// Defing the KaseiCoin contract that inherits ERC20, ERC20Detailed and ERC20Mintable
contract KaseiCoin is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(string memory name, string memory symbol, uint initial_supply) ERC20Detailed(name, symbol, 18) public {}
}