import random
import time
import os

def RunTest(rounds):
	words = ['over', 'shall', 'soil', 'better', 'lay', 'moment', 'press', 'world', 'character', 'complete', 'those', 'ago', 'speak', 'add', 'surprise', 'break', 'effect', 'mean', 'body', 'bell', 'stop', 'young', 'range', 'south', 'word', 'include', 'branch', 'tall', 'degree', 'plan', 'rule', 'head', 'field', 'type', 'fire', 'rise', 'step', 'continent', 'day', 'tube', 'settle', 'star', 'mile', 'there', 'low', 'bottom', 'born', 'trouble', 'out', 'until', 'evening', 'twenty', 'draw', 'paper', 'result', 'sight', 'drop', 'human', 'wish', 'track', 'home', 'slave', 'play', 'whole', 'please', 'perhaps', 'triangle', 'then', 'such', 'most', 'string', 'section', 'steel', 'reply', 'feet', 'usual', 'fall', 'love', 'divide', 'loud', 'paint', 'what', 'build', 'thought', 'spot', 'glass', 'my', 'hand', 'about', 'cook', 'written', 'brother', 'appear', 'get', 'rather', 'equal', 'valley', 'control', 'many', 'experiment', 'material', 'look', 'baby', 'still', 'real', 'an', 'am', 'back', 'band', 'women', 'especially', 'sand', 'warm', 'present', 'now', 'happen', 'these', 'five', 'roll', 'energy', 'a', 'want', 'smell', 'case', 'yard', 'method', 'hope', 'check', 'continue', 'past', 'wash', 'may', 'exact', 'sun', 'phrase', 'green', 'bear', 'company', 'dream', 'above', 'foot', 'famous', 'sat', 'been', 'follow', 'multiply', 'collect', 'machine', 'touch', 'power', 'money', 'tell', 'cost', 'if', 'lift', 'seven', 'arm', 'did', 'allow', 'grow', 'event', 'change', 'hear', 'proper', 'rail', 'forest', 'bad', 'time', 'dress', 'their', 'use', 'set', 'group', 'question', 'crop', 'face', 'do', 'point', 'pattern', 'thick', 'cross', 'prove', 'was', 'lot', 'surface', 'done', 'carry', 'shell', 'lady', 'numeral', 'substance', 'market', 'box', 'speech', 'figure', 'push', 'particular', 'practice', 'room', 'cent', 'quiet', 'fat', 'whose', 'never', 'music', 'kill', 'are', 'eight', 'new', 'wind', 'fraction', 'both', 'boat', 'throw', 'how', 'believe', 'common', 'industry', 'think', 'hunt', 'difficult', 'oxygen', 'receive', 'own', 'clean', 'wire', 'red', 'plant', 'compare', 'for', 'original', 'ice', 'sell', 'hot', 'distant', 'voice', "don't", 'block', 'road', 'shout', 'plural', 'leg', 'month', 'spell', 'should', 'show', 'whether', 'small', 'decimal', 'heard', 'less', 'book', 'ease', 'game', 'occur', 'read', 'ear', 'hurry', 'though', 'laugh', 'weather', 'imagine', 'clear', 'mother', 'radio', 'of', 'too', 'run', 'gun', 'fear', 'depend', 'king', 'against', 'describe', 'since', 'count', 'discuss', 'strange', 'air', 'sound', 'dear', 'win', 'snow', 'exercise', 'sugar', 'ring', 'call', 'connect', 'the', 'measure', 'place', 'window', 'pose', 'ever', 'or', 'order', 'start', 'fly', 'told', 'history', 'buy', 'just', 'motion', 'circle', 'hour', 'excite', 'example', 'solution', 'teach', 'thousand', 'from', 'produce', 'white', 'iron', 'free', 'garden', 'object', 'shoulder', 'toward', 'solve', 'one', 'science', 'ten', 'nine', 'correct', 'will', 'poem', 'stick', 'million', 'were', 'special', 'fig', 'search', 'eat', 'dance', 'several', 'through', 'plane', 'could', 'than', 'operate', 'chord', 'vowel', 'family', 'each', 'send', 'among', 'moon', 'street', 'gold', 'basic', 'pay', 'and', 'wing', 'who', 'nothing', 'pretty', 'well', 'general', 'river', 'engine', 'copy', 'simple', 'position', 'bright', 'region', 'pitch', 'jump', 'post', 'keep', 'melody', 'certain', 'base', 'wood', 'made', 'gather', 'lead', 'but', 'very', 'rest', 'metal', 'share', 'subtract', 'other', 'write', 'salt', 'feel', 'work', 'safe', 'meant', 'week', 'between', 'party', 'bone', 'save', 'they', 'ball', 'arrange', 'ride', 'nor', 'seem', 'size', 'turn', 'wide', 'corner', 'meat', 'went', 'double', 'wonder', 'best', 'them', 'learn', 'live', 'before', 'lost', 'stone', 'bat', 'near', 'piece', 'sail', 'single', 'island', 'value', 'east', 'self', 'happy', 'again', 'mine', 'began', 'travel', 'notice', 'process', 'opposite', 'second', 'coat', 'caught', 'when', 'year', 'watch', 'life', 'land', 'state', 'beauty', 'picture', 'syllable', 'tail', 'decide', 'listen', 'person', 'his', 'rain', 'open', 'truck', 'element', 'length', 'act', 'tie', 'thus', 'little', 'people', 'tiny', 'dad', 'short', 'flower', 'bed', 'rope', 'hair', 'black', 'brown', 'children', 'claim', 'joy', 'colony', 'song', 'eye', 'consonant', 'earth', 'current', 'sit', 'him', 'where', 'even', 'country', 'any', 'yes', 'cell', 'round', 'story', 'duck', 'populate', 'felt', 'interest', 'does', 'weight', 'car', 'gone', 'while', 'lake', 'cry', 'enough', 'fight', 'last', 'locate', 'town', 'provide', 'try', 'war', 'wild', 'sister', 'fresh', 'more', 'design', 'she', 'fit', 'fell', 'least', 'experience', 'heart', 'silver', 'final', 'blood', 'few', 'climb', 'move', 'fun', 'us', 'after', 'term', 'choose', 'quick', 'noise', 'not', 'instrument', 'neck', 'father', 'century', 'root', 'burn', 'stood', 'drive', 'crowd', 'grand', 'level', 'smile', 'guide', 'scale', 'instant', 'only', 'is', 'up', 'sent', 'city', 'key', 'it', 'center', 'nation', 'old', 'ground', 'feed', 'talk', 'you', 'mass', 'make', 'mind', 'farm', 'support', 'protect', 'mountain', 'product', 'men', 'heavy', 'brought', 'reason', 'visit', 'prepare', 'noun', 'why', 'sign', 'ocean', 'symbol', 'score', 'by', 'know', 'friend', 'morning', 'front', 'success', 'period', 'space', 'need', 'subject', 'top', 'sudden', 'note', 'often', 'fine', 'mix', 'some', 'parent', 'noon', 'else', 'rock', 'suffix', 'tone', 'find', 'third', 'together', 'end', 'spoke', 'job', 'match', 'except', 'animal', 'would', 'in', 'shoe', 'sleep', 'danger', 'race', 'door', 'got', 'wrote', 'big', 'much', 'modern', 'capital', 'hole', 'grew', 'station', 'mark', 'total', 'flat', 'school', 'clock', 'determine', 'right', 'to', 'art', 'so', 'doctor', 'spend', 'oh', 'path', 'part', 'broad', 'wear', 'office', 'cow', 'either', 'he', 'store', 'condition', 'man', 'straight', 'see', 'major', 'yet', 'left', 'repeat', 'fruit', 'planet', 'rose', 'paragraph', 'swim', 'mount', 'pull', 'speed', 'silent', 'dark', 'said', 'had', 'clothe', 'kind', 'chart', 'nature', 'winter', 'ask', 'let', 'tire', 'shore', 'consider', 'color', 'woman', 'port', 'row', 'always', 'course', 'arrive', 'lone', 'glad', 'view', 'shop', 'food', 'soldier', 'wheel', 'this', 'possible', 'apple', 'down', 'magnet', 'under', 'as', 'fill', 'leave', 'thin', 'on', 'same', 'inch', 'led', 'stream', 'behind', 'here', 'tool', 'list', 'offer', 'quite', 'like', 'house', 'wait', 'cut', 'close', 'took', 'three', 'dry', 'light', 'supply', 'select', 'expect', 'serve', 'bird', 'skin', 'west', 'night', 'law', 'late', 'good', 'beat', 'observe', 'season', 'hold', 'direct', 'equate', 'boy', 'edge', 'dictionary', 'train', 'bought', 'molecule', 'finish', 'gave', 'way', 'raise', 'reach', 'agree', 'anger', 'slip', 'create', 'atom', 'map', 'wrong', 'require', 'half', 'plain', 'fish', 'me', 'invent', 'stay', 'remember', 'represent', 'sea', 'card', 'chair', 'thank', 'once', 'lie', 'true', 'chief', 'probable', 'age', 'fair', 'gray', 'slow', 'govern', 'her', 'gentle', 'hill', 'quart', 'suit', 'huge', 'strong', 'miss', 'full', 'name', 'board', 'chance', 'bar', 'gas', 'busy', 'large', 'afraid', 'square', 'stand', 'die', 'mouth', 'trade', 'off', 'record', 'blue', 'take', 'village', 'with', 'say', 'trip', 'hat', 'yellow', 'drink', 'have', 'come', 'summer', 'quotient', 'spring', 'wife', 'steam', 'idea', 'your', 'hundred', 'bank', 'cotton', 'put', 'egg', 'natural', 'pound', 'walk', 'deep', 'long', 'nose', 'vary', 'can', "won't", 'held', 'bring', 'oil', 'hit', 'our', 'saw', 'sure', 'student', 'crease', 'column', 'differ', 'north', 'enter', 'ready', 'pass', 'number', 'we', 'death', 'table', 'insect', 'during', 'log', 'electric', 'dead', 'cover', 'broke', 'cause', 'rub', 'ran', 'four', 'heat', 'shape', 'first', 'side', 'form', 'must', 'area', 'water', 'cat', 'verb', 'floor', 'dollar', 'segment', 'every', 'rich', 'property', 'letter', 'sheet', 'master', 'soft', 'team', 'join', 'knew', 'pick', 'temperature', 'test', 'dog', 'page', 'coast', 'corn', 'cloud', 'favor', 'pair', 'study', 'all', 'ship', 'has', 'unit', 'poor', 'seed', 'go', 'wave', 'desert', 'answer', 'contain', 'suggest', 'at', 'catch', 'indicate', 'guess', 'found', 'stretch', 'child', 'might', 'came', 'cold', 'fast', 'sentence', 'that', 'fact', 'tree', 'separate', 'chick', 'force', 'son', 'wall', 'spread', 'system', 'captain', 'horse', 'stead', 'print', 'cool', 'matter', 'line', 'meet', 'girl', 'enemy', 'liquid', 'soon', 'minute', 'sharp', 'two', 'be', 'middle', 'forward', 'no', 'skill', 'class', 'necessary', 'also', 'high', 'sense', 'hard', 'great', 'kept', 'teeth', 'language', 'neighbor', 'sky', 'grass', 'sing', 'next', 'division', 'develop', 'begin', 'camp', 'care', 'flow', 'blow', 'similar', 'which', 'deal', 'far', 'help', 'problem', 'six', 'main', 'bit', 'finger', 'seat', 'bread', 'milk', 'early', 'give', 'charge', 'able', 'thing', 'shine', 'I', 'organ']
	WordList = []
	Inputed = []

	start = time.time()
	for i in range(rounds):
		os.system('clear')
		FirstTen = f'{words[0]} {words[1]} {words[2]} {words[3]} {words[4]} {words[5]} {words[6]} {words[7]} {words[8]} {words[9]}'
		print("\n\n\n\n\n\n")
		print(FirstTen)
		InputedTen = input()
		WordList.append(FirstTen)
		Inputed.append(InputedTen)
		del words[:10]	
	Time = time.time() - start

	InputedWords = []
	for Ten in Inputed:
		TenWords = Ten.split()
		for word in TenWords:
			InputedWords.append(word)
	GivenWords = []
	for Ten in WordList:
		TenWords = Ten.split()
		for word in TenWords:
			GivenWords.append(word)

	correct = 0
	for i in range(len(InputedWords)): 
		if InputedWords[i] == GivenWords[i]:
			correct += 1
	
	wpm = round(correct/(Time/60),2)

	Characters = 0
	for word in InputedWords:
		Characters += len(word)
	
	cpm = round(Characters/(Time/60),2)

	os.system('clear')
	print("\n\n\n\n\n\n")
	print(f'Words per min: {wpm}')
	print(f"Charcters per minute: {cpm}")
	print(f'Accuracy: {int(round(float(correct/len(InputedWords)),2)*100)}% or {correct}/{len(InputedWords)}')

if __name__ == "__main__":
	RunTest(3)











