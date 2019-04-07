alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
primes = [1299439, 1299449, 1299451, 1299457, 1299491, 1299499, 1299533, 1299541, 1299553, 1299583, 1299601, 1299631, 1299637, 1299647, 1299653, 1299673, 1299689, 1299709, 1299721, 1299743, 1299763, 1299791, 1299811, 1299817, 1299821, 1299827]
key = dict(zip(alphabets, primes))

input_string = input()
output_numbers = ""
for i in range(0,len(input_string)-1):
	output_numbers += str(key[input_string[i]]*key[input_string[i+1]]) + " "
print(output_numbers)