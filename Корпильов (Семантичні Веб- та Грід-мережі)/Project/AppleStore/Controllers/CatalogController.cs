using AppleStore.Models.Catalog;
using Microsoft.AspNetCore.Mvc;
using StoreData;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AppleStore.Controllers
{
    public class CatalogController: Controller
    {
        private IProduct _products;
        public CatalogController(IProduct products)
        {
            _products = products;
        }
        public IActionResult Index()
        {
            var productModels = _products.GetAll();
            var listingResult = productModels
                .Select(result => new ProductIndexListingModel
                {
                    Id = result.Id,
                    Image = result.Images.First(),
                    Name = result.Name,
                    Color = result.Color,
                    Country = result.Country,
                    Price = result.Price,
                    Description = result.Description
                });
            var model = new ProductIndexModel()
            {  
                Products = listingResult
            };
            return View(model);
        }

        public IActionResult Detail(int id)
        {
            if (id == 0) id=1;
            var result = _products.GetById(id);

            var model = new ProductDetailModel()
            {
                Id = result.Id,
                Images = result.Images,
                Name = result.Name,
                Color = result.Color,
                Country = result.Country,
                Description = result.Description,
                Parameters = result.Parameters,
                Price = result.Price,
                Guarantee = result.Guarantee,
                Weight = result.Weight
            };

            return View(model);
        }

        public IActionResult Partial(string sort, string filter, string find)
        {
            var productModels = _products.GetAll();

            var listingResult = productModels
                .Select(result => new ProductIndexListingModel
                {
                    Id = result.Id,
                    Image = result.Images.First(),
                    Name = result.Name,
                    Color = result.Color,
                    Country = result.Country,
                    Price = result.Price,
                    Description = result.Description,
                    Type = result.Type
                });

            if (sort != null)
            {
                if(sort=="name_up") listingResult = listingResult.OrderBy(el => el.Name);
                if(sort == "name_down") listingResult = listingResult.OrderByDescending(el => el.Name);
                if(sort == "price_up") listingResult = listingResult.OrderBy(el => el.Price);
                if(sort == "price_down") listingResult = listingResult.OrderByDescending(el => el.Price);
            }

            if (filter != null && filter != "all")
            {
                string[] filters = filter.Split('*');
                var filtered = listingResult.Where(e => filters.Contains(e.Type)).ToList();
                listingResult = filtered;
            }

            if(find != null) listingResult = listingResult.Where(el => el.Name.ToLower().Contains(find.ToLower()));

            var model = new ProductIndexModel()
            {
                Products = listingResult
            };

            
            return PartialView("Partial", model);
        }
    }
}
