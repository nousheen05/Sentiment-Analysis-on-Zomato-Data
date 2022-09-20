def eval(net,n_points,X_,Y_,device='cpu'):
  y_true=[]
  y_pred=[]
  net=net.eval().to(device)
  data=dataloader(n_points,X_,Y_)
  correct=0
  for sen, senti in data:
    batched_review=batched_review_rep([sen],len(sen))
    output,hidden=net(batched_review)
    pred=torch.argmax(output)
    y_true.append(senti)
    y_pred.append(pred)
    if(pred==senti):
      correct+=1
  confusion=confusion_matrix(y_true, y_pred)
  confusion=confusion/confusion.astype(np.float).sum(axis=1)
  df_cm=pd.DataFrame(confusion)
  sns.heatmap(df_cm, annot=True)
  plt.show()
  target_names = ['class 0', 'class 1', 'class 2']
  print(classification_report(y_true, y_pred, target_names=target_names))
  accuracy=correct/n_points
  return accuracy
