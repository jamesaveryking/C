def pigLatin(inputText):
    output = ""
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for wordGroup in inputText.split(' '):
        try:
            if(int(wordGroup[0])):
                output+=str(wordGroup) + ' '
        except:
            if(str(wordGroup) and wordGroup[len(wordGroup)-1] not in punc):
                output+=wordGroup[1:len(wordGroup)] + wordGroup[0] + 'ay '
            elif(str(wordGroup) and wordGroup[len(wordGroup)-1] in punc):
                output+=wordGroup[1:len(wordGroup)-1] + wordGroup[0] + 'ay' + wordGroup[len(wordGroup)-1] + ' '
    return output
output = pigLatin(input('Please enter your text: '))
print('The calculated output is: ' + output)