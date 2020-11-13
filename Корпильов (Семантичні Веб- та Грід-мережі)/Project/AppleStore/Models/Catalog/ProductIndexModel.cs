using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AppleStore.Models.Catalog
{
    public class ProductIndexModel
    {
        public IEnumerable<ProductIndexListingModel> Products { get; set; }
    }
}
