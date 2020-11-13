using System;
using System.Collections.Generic;
using System.Text;

namespace StoreData.Models
{
    public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public IEnumerable<Image> Images { get; set; }
        public string Color { get; set; }
        public string Country { get; set; }
        public string Parameters { get; set; }
        public double Weight { get; set; }
        public string Description { get; set; }
        public double Guarantee { get; set; }
        public double Price { get; set; }
        public string Type { get; set; }
    }
}
