// https://play.golang.org/p/N4id0caNCBk
package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"sync/atomic"
)

type countHandler struct{ n int32 }

func (h *countHandler) inc() int32 { return atomic.AddInt32(&h.n, 1) }

func routes() *http.ServeMux {
	h := countHandler{}
	mux := http.NewServeMux()
	mux.HandleFunc("/metrics", h.prometheus) // metrics endpoint
	mux.HandleFunc("/", h.json)              // hit this to increment the counter
	return mux
}

// increments the counter
func (h *countHandler) json(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, "%d", h.inc()) // Surprisingly valid JSON
}

// exports the counter to be scraped by prometheus
func (h *countHandler) prometheus(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, `# HELP count_total shows the in-memory count
# TYPE count_total counter
count_total %d`, h.n)
}

func main() { log.Fatal(http.ListenAndServe(":"+os.Getenv("PORT"), routes())) }
