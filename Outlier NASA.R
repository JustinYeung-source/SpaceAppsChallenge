accepted_values <- NULL    
rejected_values <- NULL
accepted <- 0 
rejected <- 0 

for (x in (1:length(DAWS))){
  if(DAWS[x] > 86.66067){
  accepted <- accepted + 1 
  accepted_values[x] <- DAWS[x]}
  else{rejected_values[x] <- DAWS[x]}}

hist(DAWS)

mean(DAWS)

for (x in (1:length(DAWS))){
  if (71.93381 < DAWS[x] && DAWS[x] < 101.38754){
    accepted_values[x] <- DAWS[x]
    accepted <- accepted + 1
  }else{ 
    rejected_values[x] <- DAWS[x] 
    rejected <- rejected + 1
  } 
  
}
results <- list(c(accepted_values, rejected_values))
return(results)

}      