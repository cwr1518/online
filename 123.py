from graph import Graph
from DQN import DeepQNetwork
import match
import numpy as np

filename="11.txt"
graph=Graph(filename)
H=100000
lmin=30
lmax=50
actions=[0,1]
all_reward=0
def run_net():
    t=0
    graph.time_update()
    graph.input_new_point(t)
    l_num = len(graph.left)
    r_num = len(graph.right)
    global all_reward
    reward=0
    l,t = 1,1
    l = lmin
    while t<H:
        graph.time_update()
        graph.input_new_point(t)
        state=np.array([l_num,r_num,match.fake_matching(graph.left,graph.right,graph.edge),l])
        action=RL.choose_action(state)
        if action==0:
            l_num = len(graph.left)
            r_num = len(graph.right)
            reward=0
            l=l+1
            state_ = np.array([l_num, r_num, match.fake_matching(graph.left, graph.right, graph.edge), l])
            RL.store_transition(state, action, reward, state_)
            t=t+1
        else:
            reward = match.matching(graph.left, graph.right, graph.edge)
            print("r",reward)
            l_num = len(graph.left)
            r_num = len(graph.right)
            l=0
            state_=np.array([l_num,r_num,match.fake_matching(graph.left,graph.right,graph.edge),l])
            RL.store_transition(state, action, reward, state_)
            t=t+1
        if (t > 200) and (t % 5 == 0):
            print("sss")
            RL.learn()
        all_reward=reward+all_reward
        print("得分",all_reward,"轮数",t)



if __name__=='__main__':
    RL = DeepQNetwork(2, 4,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      output_graph=True
                      )
    run_net()

