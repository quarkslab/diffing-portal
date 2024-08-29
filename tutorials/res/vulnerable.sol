// SPDX-License-Identifier: MIT

pragma solidity 0.8.25;

contract SimpleToken {
    mapping(address => int) public balances;
    
    constructor() {
        balances[msg.sender] += 1000e18;
    }
    
    function sendToken(address _recipient, int _amount) public {
        balances[msg.sender] -= _amount;
        balances[_recipient] += _amount;
    }   
}
