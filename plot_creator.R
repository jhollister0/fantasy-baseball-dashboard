setwd("/Users/jameshollister/Documents/GitHub/fantasy-baseball-dashboard")
data <- read.csv("FantasyResults.csv")

library(ggplot2)
library(grDevices)

p <- ggplot(data, aes(x=k_pitch, y=k_hit)) + 
  geom_point() +
  geom_smooth(method = "lm", se=FALSE) +
  ggtitle("Pitching vs. Hitting Strikeouts") +
  xlab("Strikeouts Hitting") +
  ylab("Strikeouts Pitching")

ggsave("TestPlot.pdf", plot=p)
