from graph import Graph
from DQN import DeepQNetwork
import match
import numpy as np
import time

time_number=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
logfile=str("DQNF"+time_number+".txt")
file_handle=open(logfile,mode="w")
filename="11.txt"
graph=Graph(filename)
H=10000
lmin=30
lmax=50
actions=[0,1]
all_reward=0
record=0
record_old=0
def run_net():
    t=0
    graph.time_update()
    graph.input_new_point(t)
    l_num = len(graph.left)
    r_num = len(graph.right)
    global all_reward,record_old
    reward=0
    l,t = 0,1
    while t<H:
        l_num = len(graph.left)
        r_num = len(graph.right)
        state=np.array([l_num,r_num,match.fake_matching(graph.left,graph.right,graph.edge),l])
        action=RL.choose_action(state)
        if action==0:
            graph.time_update()
            graph.input_new_point(t)
            l_num_ = len(graph.left)
            r_num_ = len(graph.right)
            reward=0
            l=graph.existing_time()
            state_ = np.array([l_num_, r_num_, match.fake_matching(graph.left, graph.right, graph.edge), l])
            RL.store_transition(state, action, reward, state_)
            t=t+1
        else:
            reward = match.matching(graph.left, graph.right, graph.edge)
            print("r",reward,"左边",l_num,"右边",r_num)
            graph.time_update()
            graph.input_new_point(t)
            l_num_ = len(graph.left)
            r_num_ = len(graph.right)
            l=graph.existing_time()
            state_=np.array([l_num_,r_num_,match.fake_matching(graph.left, graph.right, graph.edge),l])
            RL.store_transition(state, action, reward, state_)
            t=t+1
        if (t > 200) and (t % 30 == 0):
            print("sss")
            RL.learn()
        all_reward=reward+all_reward
        if t%1000==0:
            record=all_reward
            file_handle.write("得分"+str(all_reward)+" "+"轮数"+str(t)+"\n")
            file_handle.write("比上一千轮增加："+str(record-record_old)+"\n")
            file_handle.write("\n")
            record_old=record
        print("得分",all_reward,"轮数",t)



if __name__=='__main__':
    RL = DeepQNetwork(2, 4,
                      learning_rate=0.001,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      output_graph=True,
                      restore=True
                      )
    run_net()
    file_handle.close()
    RL.saver.save(RL.sess,"./model_saved/model_test")
    RL.plot_cost()

