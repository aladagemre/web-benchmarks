package main

import (
	"context"
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/jackc/pgx/v5/pgxpool"
)

var db *pgxpool.Pool

func main() {
	var err error
	dsn := "postgres://robynuser:robynpass@postgres:5432/robyn_db"
	db, err = pgxpool.New(context.Background(), dsn)
	if err != nil {
		panic(fmt.Sprintf("Failed to connect to DB: %v", err))
	}
	defer db.Close()

	r := gin.Default()

	r.GET("/users", func(c *gin.Context) {
		var count int
		err := db.QueryRow(context.Background(), `SELECT COUNT(*) FROM "user"`).Scan(&count)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, gin.H{"count": count})
	})

	r.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, "Gin + PostgreSQL is ready 🚀")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8004"
	}
	r.Run("0.0.0.0:" + port)
}
