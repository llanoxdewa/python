############ kita harus meloncati awan #####################

# max lompatan = 2
# 0 awan putih 
# 1 awan hitam 
c = [0,0,1,0,0,1,0]
#c = [0,1,0,0,0,1,0]


def jump_the_cloud(cloud):
	jump = 0
	while len(cloud)>2:
		nexter = 2 if c[2]==0 else 1
		cloud = cloud[nexter:]
		jump += 1
	return jump + len(cloud) - 1

print(jump_the_cloud(c))
































