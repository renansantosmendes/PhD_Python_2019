setwd("/home/renansantos/Área de Trabalho/Experimentos")

solutions <- read.csv('new_solutions.csv',header = FALSE, sep=",")
c <- cor(solutions, method = "kendall")
d <- as.dist(c, diag = FALSE)
        
plot(hclust(d, method="ward"))