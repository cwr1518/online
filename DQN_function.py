from graph import Graph
from DQN import DeepQNetwork
import match
import numpy as np
import time
import os
import tensorflow as tf
module_path = os.path.dirname(__file__)

filename="16_15_1.5.txt"
H=15000
lmin=30
lmax=50
actions=[0,1]

def run_net():
    all_reward=0
    record=0
    record_old=0
    t=0
    graph.time_update()
    graph.input_new_point(t)
    l_num = len(graph.left)
    r_num = len(graph.right)
    reward=0
    l_l,l_r,t = 0,0,1
    while t<H:
        l_num = len(graph.left)
        r_num = len(graph.right)
        state=np.array([l_num,r_num,match.fake_matching(graph.left,graph.right,graph.edge),l_l,l_r])
        action=RL.choose_action(state)
        if action==0:
            graph.time_update()
            graph.input_new_point(t)
            l_num_ = len(graph.left)
            r_num_ = len(graph.right)
            reward=0
            l_l,l_r=graph.existing_time()
            state_ = np.array([l_num_, r_num_, match.fake_matching(graph.left, graph.right, graph.edge), l_l,l_r])
            RL.store_transition(state, action, reward, state_)
            t=t+1
        else:
            reward = match.matching(graph.left, graph.right, graph.edge)
            print("r",reward,"左边",l_num,"右边",r_num)
            graph.time_update()
            graph.input_new_point(t)
            l_num_ = len(graph.left)
            r_num_ = len(graph.right)
            l_l,l_r=graph.existing_time()
            state_=np.array([l_num_,r_num_,match.fake_matching(graph.left, graph.right, graph.edge),l_l,l_r])
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
    netsaver="./model_saved_16_10/model_test_10"
    netsavefold="./model_saved_16_10"
    for o in range(2):
        tf.reset_default_graph()
        RL = DeepQNetwork(2, 5,
                      learning_rate=0.001,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      output_graph=True,
                      restore=True,
                      if_learning=False,
                      netsavefold=netsavefold
                      )
        graph=Graph(filename)
        time_number=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        logfile=str(module_path+"/DQNlog/"+"DQNF"+filename+time_number+".txt")
        file_handle=open(logfile,mode="w")
        run_net()
        RL.saver.save(RL.sess,netsaver)
        file_handle.close()

    RL.plot_cost()

