def train_a_batch(net,opt,loss_fn,n_points,device='cpu'):

  net.train().to(device)  #sets the mode to training
  opt.zero_grad()         #resetting all grad values to zero
  
  rev,rat,batched_input,batched_output,reviews_len=batched_dataloader(n_points,X_train,Y_train)
  output,hidden=net(batched_input,rev_len=reviews_len)

  loss=loss_fn(output,batched_output)

  loss.backward()
  opt.step()

  return loss

def train_setup(net,opt,lr=0.01,n_batches=100,batch_size=10,momentum=0.05,display_frequency=5,device='cpu',model_num='zomato A'):
  net=net.to(device)
  loss_fn=nn.NLLLoss()
  loss_plot=[]
  loss_arr=np.zeros(n_batches)

  for i in tqdm(range(n_batches),desc='Batch Completion'):
    loss_arr[i]=train_a_batch(net,opt,loss_fn,batch_size,device)
    
    if i%display_frequency==0:
      loss_plot.append(loss_arr[i])
      plt.plot(loss_plot)
      plt.show()
    
    if (i+1)%50==0:
      PATH="/content/drive/MyDrive/"+model_num+"-"+str(i)
      torch.save(net.state_dict(), PATH)
      print("model saved version : ",(i+1)/50)
  
  return loss_arr
