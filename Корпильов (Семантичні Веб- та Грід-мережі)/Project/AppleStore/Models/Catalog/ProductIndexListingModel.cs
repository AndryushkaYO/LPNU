using StoreData.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AppleStore.Models.Catalog
{
    public class ProductIndexListingModel
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public Image Image { get; set; }
        public string Color { get; set; }
        public string Country { get; set; }
        public string Description { get; set; }
        public string Type { get; set; }
        public double Price { get; set; }
    }
}

