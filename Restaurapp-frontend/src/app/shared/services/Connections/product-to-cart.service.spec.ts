import { TestBed } from '@angular/core/testing';

import { ProductToCartService } from './product-to-cart.service';

describe('ProductToCartService', () => {
  let service: ProductToCartService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProductToCartService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
