# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util,random

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0
     
    for i in range(iterations):
    	tem=self.values.copy()
    	states=self.mdp.getStates()
    	#state=self.mdp.getStartState()
    	for state in states:
    		if self.mdp.isTerminal(state):
    			continue
    	#while not self.mdp.isTerminal(state):
    		actions=self.mdp.getPossibleActions(state)
    		maxi=float("-inf")
    		for j in actions:
    			trans=self.mdp.getTransitionStatesAndProbs(state,j)
    			sigma=self.getQValue(state,j)
    			#for k in trans:
    				#print trans[1]
    				#sigma+=k[1]*(self.mdp.getReward(state,j,k[0])+self.discount*self.values[k[0]])
    			if sigma>maxi:
    				maxi=sigma
    		tem[state]=maxi
    		#print "updtd"
    		#self.values=tem
    		state=random.choice(trans)[0]
    	self.values=tem
    		#print state
    "*** YOUR CODE HERE ***"
    
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    trans=self.mdp.getTransitionStatesAndProbs(state,action)
    sigma=0
    for i in trans:
    	sigma+=i[1]*(self.mdp.getReward(state,action,i[0])+self.discount*self.values[i[0]])
    return sigma
    util.raiseNotDefined()

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    actions=self.mdp.getPossibleActions(state)
    a=None
    v=float("-inf")
    for i in actions:
    	tem=self.getQValue(state,i)
    	if tem>v:
    		v=tem
    		a=i
    return a
    util.raiseNotDefined()

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  
