# reference for dxl servos read + write functions

## function structures:

Result, Error = packetHandler.writeXByteTxRx(portHandler, DXL_ID, ADDR, Value)

Value, Result, Error = packetHandler.readXBytesTxRx(portHandler, DXL_ID, ADDR)

## values:

- portHandler: object to help send data to the servo
- DXL_ID: ID number that tells the portHandler which servo to read or write to (configure servos IDs with dynamixel software)
- ADDR: address in memory to read value from or write value to (specific memory locations are for specific useful values like current position, etc.)
- Value: value to be read from or written to memory at address ADDR
- Result: object containing info about if the read / write worked (if Result = COMM_SUCCESS then the read / write worked)
	- use packetHandler.getTxRxResult(Result) to get string of the result
- Error: object containing info about any errors if any happen (if Error != 0 then there was an error with the read / write)
	- use packetHandler.getTxRxError(Error) to get a string of the error