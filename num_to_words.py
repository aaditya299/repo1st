import math

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
exceptionTens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
increasingMagnitude = ["", "", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

num = input("Enter the number: ")

def chunkMaker(num: str) -> list[str]:
    chunks = []
    start = 0
    
    while start < len(num) and num[start] == '0':
        start += 1
    
    length = len(num) - start
    end = (start + length % 3) if length % 3 > 0 else (start + 3)

    for _ in range(math.ceil(length / 3)):
        chunks.append(num[start:end])
        start = end
        end += 3
    
    return chunks

def chunkToWords(chunk: str):
    chunkList = []

    while len(chunk) < 3:
        chunk = '0' + chunk
    
    hundredsInChunk = int(chunk[0])
    tensInChunk = int(chunk[1])
    onesInChunk = int(chunk[2])

    if hundredsInChunk > 0:
        chunkList.append(f"{ones[hundredsInChunk]} hundred")
    if tensInChunk > 1:
        chunkList.append(f"{tens[tensInChunk]}")
    elif tensInChunk == 1:
        chunkList.append(exceptionTens[onesInChunk])
        return " ".join(chunkList)
    if onesInChunk > 0:
        chunkList.append(ones[onesInChunk])
    
    return " ".join(chunkList)

def NumToWords(num):
    chunks = chunkMaker(num)
    if len(chunks) == 0:
        return "Please try some other number!"
    
    finalChunks = []
    for i in range(len(chunks)):
        result = chunkToWords(chunks[i])
        if result != "":
            finalChunks.append(result)
            finalChunks[len(finalChunks) - 1] += (" " + increasingMagnitude[len(chunks) - i])

    return " ".join(finalChunks).strip()

result = NumToWords(num)
print(result)

# It doesn't support decimals yet. But I think I'll leave it at that. :)