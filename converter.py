import struct

def float_to_ieee754(value):
    # Pack the float into 4 bytes (32 bits) and unpack as an unsigned integer
    packed = struct.pack('!f', value)
    integer_val = struct.unpack('!I', packed)[0]
    
    # Convert to 32-bit binary string
    binary_str = f"{integer_val:032b}"
    
    # Extract components
    sign_bit = binary_str[0]
    exponent_bits = binary_str[1:9]
    mantissa_bits = binary_str[9:]
    
    # Calculate actual exponent value (Bias is 127 for single precision)
    biased_exp = int(exponent_bits, 2)
    actual_exp = biased_exp - 127
    
    return {
        "decimal": value,
        "binary_32": binary_str,
        "sign": sign_bit,
        "exponent_biased": exponent_bits,
        "exponent_actual": actual_exp,
        "mantissa": mantissa_bits
    }

if __name__ == "__main__":
    test_value = 5.75
    result = float_to_ieee754(test_value)
    
    print(f"--- IEEE 754 Single-Precision Analysis for {result['decimal']} ---")
    print(f"Full 32-bit Binary : {result['binary_32']}")
    print(f"Sign Bit (S)       : {result['sign']} ({'+' if result['sign'] == '0' else '-'})")
    print(f"Exponent (E)       : {result['exponent_biased']} (Biased: {int(result['exponent_biased'], 2)}, Actual: {result['exponent_actual']})")
    print(f"Mantissa (M)       : {result['mantissa']}")
