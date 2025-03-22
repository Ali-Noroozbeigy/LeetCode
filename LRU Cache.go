package main

import (
	"fmt"
	"math"
)

type LRUCache struct {
	data     map[int]int
	timeline map[int]int
	capacity int
	counter  int
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		data:     make(map[int]int),
		timeline: make(map[int]int),
		counter:  0,
	}
}

func (lru *LRUCache) Get(key int) int {
	value, ok := lru.data[key]
	if !ok {
		return -1
	}
	lru.timeline[key] = lru.counter
	lru.counter++
	return value
}

func (lru *LRUCache) evict(key int, value int) {
	minTime := math.Inf(1)
	var keyToRemove int
	for tempKey, _ := range lru.data {
		time := lru.timeline[tempKey]
		if float64(time) < minTime {
			minTime = float64(time)
			keyToRemove = tempKey
		}
	}
	delete(lru.data, keyToRemove)
	delete(lru.timeline, keyToRemove)
	lru.data[key] = value
	lru.timeline[key] = lru.counter
	lru.counter++
}

func (lru *LRUCache) Put(key int, value int) {
	if _, ok := lru.data[key]; ok{
		lru.data[key] = value
		lru.counter = lru.counter + 1
	}else if len(lru.data) < lru.capacity {
		lru.data[key] = value
		lru.timeline[key] = lru.counter
		lru.counter = lru.counter + 1
	} else {
		lru.evict(key, value)
	}
}

func main() {
	lru := Constructor(2)
	lru.Put(1, 0)
	lru.Put(2, 2)
	fmt.Println("data: ", lru.data)
	fmt.Println("timeline", lru.timeline)
	fmt.Println(lru.Get(1))
	fmt.Println("timeline", lru.timeline)
	lru.Put(3, 3)
	fmt.Println(lru.Get(2))
	lru.Put(4, 4)
	fmt.Println(lru.Get(1))
	fmt.Println(lru.Get(3))
	fmt.Println(lru.Get(4))
}
