// -*- tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 2 -*-
// vi: set et ts=4 sw=2 sts=2:
#ifndef DUNE_P13DLOCALFINITEELEMENT_HH
#define DUNE_P13DLOCALFINITEELEMENT_HH

#include <dune/localfunctions/lagrange/lagrangeprism.hh>

#warning This header is deprecated

namespace Dune
{

  /** \brief First-order Lagrangian finite element on a prism
   *
   * \deprecated Please use LagrangePrismLocalFiniteElement<D,R,2> instead!
   */
  template<class D, class R>
  using PrismP1LocalFiniteElement
    [[deprecated("use LagrangePrismLocalFiniteElement instead")]]
    = LagrangePrismLocalFiniteElement<D,R,1>;

}

#endif
