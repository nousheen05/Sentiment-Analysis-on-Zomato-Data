class BiLSTM_net(nn.Module):
  def __init__(self,vocab_size, hidden_size,num_layers,embedding_dim, output_size,dropout):
    super(BiLSTM_net,self).__init__()
    self.hidden=hidden_size
    self.num_layers=num_layers
    self.embedding=nn.Embedding(vocab_size,embedding_dim)
    self.lstm_cell=nn.LSTM(embedding_dim,hidden_size,num_layers=num_layers,dropout=0.3,bidirectional=True,batch_first=True)
    self.dropout=nn.Dropout(dropout)
    self.h2o=nn.Linear(hidden_size*2,output_size)
    self.softmax=nn.LogSoftmax(dim=2)

  def forward(self,input_,hidden_=None,batch_size=1,rev_len=None,device='cpu'):
    emb=self.embedding(input_.to(torch.long))
    out,hidden=self.lstm_cell(emb,hidden_)
    hidden=self.dropout(torch.cat((hidden[0][-2:-1,:,:],hidden[0][-1:,:,:]),dim=2))
    output=self.h2o(hidden)
    output=self.softmax(output)
    return output.view(-1,3),hidden

  def analyse_forward(self,input_,hidden_=None,batch_size=1,rev_len=None,device='cpu'):
    seq_out=[]
    emb=self.embedding(input_.to(torch.long))
    out,hidden=self.lstm_cell(emb,hidden_)
    print("Input",input_.size())
    print("Hidden",hidden[0].size())
    print("Cell",hidden[1].size())
    print("Output",out.size())
    print(out[-1]==hidden[0])
    for i in out:
      output=self.dropout(torch.cat((i[-2:-1,:,:],i[-1:,:,:]),dim=2))
      output=self.h2o(output)
      output=self.softmax(output)
      seq_out.append(output.view(-1,3),hidden)
    return seq_out
