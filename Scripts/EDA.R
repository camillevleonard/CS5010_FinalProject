library(plyr)
library(dplyr)

data <- read.csv("MainData.csv")

data %>% count(cause_name)
