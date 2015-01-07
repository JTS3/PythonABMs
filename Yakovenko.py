#This program implements something I saw Yakovenko of UMD show in a presentation about inequality.
#The random graph structure of the exchanges done during every tick produces a final histogram that is decidedly skewed.
# The skew is motivated by the zero lower bound on individual's balances.

# Set up the list of agents, make it n agents large, give each agent 1
agents = []
n=100                        #number of agents
for builder in range(n):
    agents.append(1)

# Move 1 dollar from agent i's balance to agent j's balance during each of t ticks
import random
t = 10000000                    #ticks in simulation
for ticks in range(t):
    i = random.randint(0, len(agents)-1)  #randint draws between 0 and len(agents)-1 inclusively. 
    j = random.randint(0, len(agents)-1)  # The -1 after len(agents) keeps you within the elements of the list. 
    if agents[i] > 0:              #only agents with non-zero balances can be asked to give. 
        agents[i] = agents[i] - 1  #remove 1 from agent i's balance
        agents[j] = agents[j] + 1  #add 1 to agent j's balance

#print agents



#OUTPUT
# Make a histogram which tallies up the number of agents with given balances.
# Note that in the for loop, the range is given by max(agents)+1
# because max(agents) is largest element in agents,
# range(x) goes from 0 to x without including x.
print ""
print "After", t ,"ticks with", n,"agents, the distribution is:"
print ""
print "balance | count of agents | freq"
for balance in range(max(agents)+1):
    junk = agents.count(balance)
    print balance,"|", junk,"|", (float(junk) / len(agents))
print ""