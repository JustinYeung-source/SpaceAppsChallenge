
# Location ONE 

site_DAWS<- c 

attach(dataset2_full)

DAWS <- as.numeric(dataset2_full) 
mean(DAWS)
median(DAWS)
fivenum(DAWS) 
t.test(DAWS, conf.level=0.99) 
sd(DAWS)



accepted_values <- NULL    
rejected_values <- NULL
accepted <- 0 
rejected <- 0  

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


Imma_outlier <- function(DAWS){ 
  
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



fivenum() 
mean() 
sd() 

# t test by row to determine the location effect 


t.test(conf.level=0.99)




  
))
