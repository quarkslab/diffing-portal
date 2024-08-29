// SPDX-License-Identifier: MIT

pragma solidity 0.8.25;

contract SimpleToken {
    mapping(address => uint) public balances;
    
    constructor() {
        balances[msg.sender] += 1000e18;
    }
    
    function sendToken(address _recipient, uint _amount) public {
        balances[msg.sender] -= _amount;
        balances[_recipient] += _amount;
    }   
}
