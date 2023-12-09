module Main (main) where

import Data.List.Split

strToInt :: String -> Int
strToInt x = read x

getNext :: [Int] -> Int
getNext theList
   | all (==0) theList = 0
   | otherwise = last theList + (getNext (zipWith (-) (tail theList) theList))


main :: IO ()
main = do
  contents <- readFile "input.txt"
  let valuesAsStr = map (splitOn " ") (lines contents)
  let intValues = map (map strToInt) valuesAsStr
  let predictions = map getNext intValues
  print (sum predictions)
