bird = [1,2,3,4,5,4,3,2,1,3,4] # hasil harus 3

# def countBird(bird):
# 	highest_count,highest_bird = 0,0
# 	for i in range(1,6):
# 		count = len([b for b in bird if b == i])
# 		if highest_count < count:
# 			highest_count = count
# 			highest_bird = i
# 	return highest_bird

def countBird(bird):
	bird_count = [0] * 5 # bird_count = [0,0,0,0,0]
	for b in bird:
		bird_count[b-1] += 1 # bird_ count = 
	print(bird_count)
	#return bird_count.index(max(bird_count)) + 1
print(bird)
countBird(bird)
	


